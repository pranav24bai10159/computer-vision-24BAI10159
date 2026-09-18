import argparse
import sys
from pathlib import Path
from src.image_io import read_image, save_image
from src.enhancement import to_grayscale, enhance_contrast
from src.edge_detection import detect_edges
from src.analysis import build_report, save_report

def main():
    parser = argparse.ArgumentParser(description="Simple Computer Vision Image Toolkit")
    parser.add_argument("--input", required=True, help="Path to input image")
    parser.add_argument("--output", default="output", help="Directory to store processed results")
    args = parser.parse_args()

    try:
        image = read_image(args.input)
        gray = to_grayscale(image)
        enhanced = enhance_contrast(gray)
        edges = detect_edges(enhanced)
        
        out = Path(args.output)
        out.mkdir(parents=True, exist_ok=True)
        
        save_image(out / "01_grayscale.jpg", gray)
        save_image(out / "02_enhanced.jpg", enhanced)
        save_image(out / "03_edges.jpg", edges)
        save_report(out / "analysis.json", build_report(image, enhanced, edges))
        
        print("Processing completed successfully.")
        print(f"Results saved in: {out}")
    except (FileNotFoundError, ValueError, OSError) as e:
        print(f"Error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Error: An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
