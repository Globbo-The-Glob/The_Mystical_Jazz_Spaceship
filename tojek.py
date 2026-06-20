#!/usr/bin/env python3
import re
import sys
from pathlib import Path
from datetime import datetime
import shutil

# === FUNCTIONS ===

def fix_math_blocks(text):
    """
    Ensure $$...$$ block math has blank lines above/below.
    Inline $$...$$ stays untouched.
    """
    lines = text.splitlines()
    output = []
    for line in lines:
        stripped = line.strip()
        if re.fullmatch(r"\$\$.*\$\$", stripped):
            output.append("")
            output.append(stripped)
            output.append("")
        else:
            output.append(line)
    return "\n".join(output)


def slugify(text):
    """Convert title to URL-friendly slug."""
    text = text.strip().lower()
    text = re.sub(r"\s+", "-", text)       # spaces → hyphens
    text = re.sub(r"[^a-z0-9\-]", "", text)  # remove special chars
    return text


def add_frontmatter(text, title):
    """Add Jekyll frontmatter to the Markdown."""
    now = datetime.now().astimezone()
    date_str = now.strftime("%Y-%m-%d %H:%M:%S %z")
    permalink = "/" + slugify(title)
    frontmatter = f"""---
layout: payge
title:  "{title}"
date:   {date_str}
categories: jekyll update
permalink: {permalink}
---

"""
    return frontmatter + text


def copy_images(text, vault_root, dest_dir):
    """
    Find all ![[image.png]] references (with or without subdirectories),
    copy images to a single folder, and rewrite Markdown links
    for Jekyll.
    """
    Path(dest_dir).mkdir(parents=True, exist_ok=True)

    def replace_image(match):
        img_path = match.group(1).strip()
        img_name = Path(img_path).name
        dst_path = Path(dest_dir) / img_name

        src_path = None

        # Try exact path first
        candidate = Path(vault_root) / img_path
        if candidate.exists():
            src_path = candidate

        # Try zimages folder (various capitalizations)
        for zimages_name in ["zimages", "zImages", "zImagesz", "z Images"]:
            if not src_path:
                candidate = Path(vault_root) / zimages_name / img_name
                if candidate.exists():
                    src_path = candidate

        # Try images folder
        if not src_path:
            candidate = Path(vault_root) / "images" / img_name
            if candidate.exists():
                src_path = candidate

        # Search recursively as last resort
        if not src_path:
            found_files = list(Path(vault_root).rglob(img_name))
            if found_files:
                src_path = found_files[0]

        if not src_path:
            print(f"WARNING: Image not found in vault: {img_path}")
            return match.group(0)  # Return original if not found

        shutil.copy2(src_path, dst_path)
        print(f"Copied image: {src_path} -> {dst_path}")

        # Return Jekyll Markdown image link
        return f"![{Path(img_name).stem}](/images/{img_name})"

    # Replace all ![[...]] references
    new_text = re.sub(r'!\[\[([^\]]+?)\]\]', replace_image, text)
    return new_text


def convert_file(input_path, vault_root, posts_dir, images_dir):
    input_path = Path(input_path)
    vault_root = Path(vault_root)

    # If path doesn't have .md extension, try adding it
    if input_path.suffix != ".md":
        input_path_with_md = input_path.with_suffix(input_path.suffix + ".md")
    else:
        input_path_with_md = input_path

    # If path doesn't exist as-is, try relative to vault_root
    if not input_path_with_md.exists():
        vault_relative = vault_root / input_path_with_md
        if vault_relative.exists():
            input_path = vault_relative
        else:
            # Try without .md extension added
            vault_relative_orig = vault_root / input_path
            if vault_relative_orig.exists():
                input_path = vault_relative_orig
            else:
                print(f"ERROR: File not found:")
                print(f"  Tried: {input_path_with_md}")
                print(f"  Tried: {vault_relative}")
                print(f"  Tried: {vault_relative_orig}")
                return
    else:
        input_path = input_path_with_md

    text = input_path.read_text()

    # Fix math blocks
    converted_text = fix_math_blocks(text)

    # Copy images and rewrite Markdown links
    converted_text = copy_images(converted_text, str(vault_root), images_dir)

    # Generate title from filename
    title = input_path.stem.replace("-", " ").title()

    # Add frontmatter
    final_text = add_frontmatter(converted_text, title)

    # Prepare output filename: YYYY-MM-DD-slug.md
    now = datetime.now().astimezone()
    date_str_file = now.strftime("%Y-%m-%d")
    slug_title = slugify(title)
    output_filename = f"{date_str_file}-{slug_title}.md"

    # Save to _posts folder
    posts_dir = Path(posts_dir)
    posts_dir.mkdir(parents=True, exist_ok=True)
    output_file = posts_dir / output_filename
    output_file.write_text(final_text)
    print(f"Converted '{input_path}' -> '{output_file}'")


# === MAIN ===

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 tojek.py <file.md> [vault_root] [posts_dir] [images_dir]")
        sys.exit(1)

    # File to convert
    input_file = sys.argv[1]

    # Use command-line args or defaults
    vault_root = sys.argv[2] if len(sys.argv) > 2 else "/home/globbo/Documents/The State of Affairs"
    posts_dir = sys.argv[3] if len(sys.argv) > 3 else "/home/globbo/TMJSS/_posts"
    images_dir = sys.argv[4] if len(sys.argv) > 4 else "/home/globbo/TMJSS/images"

    convert_file(input_file, vault_root, posts_dir, images_dir)