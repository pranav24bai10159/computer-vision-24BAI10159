# Simple Computer Vision Image Toolkit

A command-line Computer Vision project using Python and OpenCV.

## Features
- Grayscale conversion
- CLAHE contrast enhancement
- Canny edge detection
- Image statistics and JSON report
- Automated tests
- No GUI required

## Setup

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

## Run

```bash
python main.py --input input/sample.jpg --output output
```

Use your own image:

```bash
python main.py --input path/to/image.jpg --output output
```

## Test

```bash
pytest -q
```

## Output

The program creates `01_grayscale.jpg`, `02_enhanced.jpg`, `03_edges.jpg`, and `analysis.json` in the output folder.

## Project Structure

```text
main.py
requirements.txt
statement.md
src/
tests/
input/
output/
screenshots/
docs/
```

## Non-Functional Requirements
- Usability: simple command-line interface.
- Reliability: validates missing or unreadable images.
- Maintainability: separate processing modules.
- Performance: OpenCV processes one image at a time.
- Error handling: readable terminal errors.

## Future Enhancements
Batch processing, interactive thresholds, histogram visualization, and automatic parameter selection.
