from PyPDF2 import PdfReader

def extract_city_data(file_path):
    reader = PdfReader(file_path)
    city_data = {}

    city_names = [
        "Mumbai", "Kolhapur", "Latur", "Aurangabad", "Osmanabad",
        "Amravati", "Ahmednagar", "Pune", "Nagpur", "Nashik"
    ]

    current_city = None
    for page in reader.pages:
        text = page.extract_text()
        lines = text.split("\n")
        for line in lines:
            if any(city in line for city in city_names):
                current_city = next(city for city in city_names if city in line)
                city_data[current_city] = ""
            if current_city:
                city_data[current_city] += line + " \n "

    return city_data

def format_city_data(city_data):
    formatted_data = ""
    for city, data in city_data.items():
        formatted_data += f"### {city}\n```\n{data}```\n\n"
    return formatted_data

file_path = "E:\\Political analytics\\City profiles of maharastra.pdf"
city_data = extract_city_data(file_path)
formatted_data = format_city_data(city_data)
#print(type(city_data))
#print(type(formatted_data))
#print(city_data.get("Mumbai"))