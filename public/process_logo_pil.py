from PIL import Image

def process_logo():
    img = Image.open('logo.png').convert("RGBA")
    data = img.getdata()

    new_data = []
    for item in data:
        r, g, b, a = item
        
        # Check if close to background color (217, 220, 223)
        if abs(r - 217) < 30 and abs(g - 220) < 30 and abs(b - 223) < 30:
            new_data.append((255, 255, 255, 0)) # Transparent
        # Check if it's dark text (EverglowLabs dark blue text)
        elif r < 100 and g < 100 and b < 150:
            new_data.append((255, 255, 255, a)) # Make text white
        else:
            new_data.append(item)

    img.putdata(new_data)
    
    # Trim the transparent borders
    bbox = img.getbbox()
    if bbox:
        img = img.crop(bbox)
        
    img.save('logo_clean.png')

if __name__ == '__main__':
    process_logo()
    print("Saved logo_clean.png")
