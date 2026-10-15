import cv2


def decode_qr_from_path(image_path: str) -> dict:
    img = cv2.imread(image_path)
    if img is None:
        return _fail(f"Could not open image: {image_path}")

    detector = cv2.QRCodeDetector()
    data, points, _ = detector.detectAndDecode(img)

    if not data:
        # Retry after grayscale + upscale, helps with low-res images
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        upscaled = cv2.resize(gray, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
        data, points, _ = detector.detectAndDecode(upscaled)

    if not data:
        return _fail("No QR code detected in the image.")

    bbox = None
    if points is not None:
        pts = points[0]
        x_coords = [p[0] for p in pts]
        y_coords = [p[1] for p in pts]
        x, y = min(x_coords), min(y_coords)
        w, h = max(x_coords) - x, max(y_coords) - y
        bbox = (int(x), int(y), int(w), int(h))

    return {
        "success": True,
        "data": data,
        "type": "QRCODE",
        "bbox": bbox,
        "error": None,
    }


def _fail(msg: str) -> dict:
    return {"success": False, "data": None, "type": None, "bbox": None, "error": msg}


if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python qr_decoder.py <path_to_qr_image>")
        sys.exit(1)
    result = decode_qr_from_path(sys.argv[1])
    print(result)