import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.DataFrame({
    "city_name": ["Mumbai", "Kolhapur", "Latur", "Aurangabad", "Osmanabad", "Amravati", 
                  "Ahmednagar", "Pune", "Nagpur", "Nashik"],
    "population": [12.5e6, 549236, 396955, 1175116, 111825, 646801, 
                          350859, 3124458, 2405665, 1486053],
    "hindu_population": [67.39,90,90,51.07,85,61.87,75.69,90,90,85.91],
    "muslim_population": [18.56,7,8,30.79,10.51,23.7,15.64,6,7.84,8.91],
    "sex_ratio": [832, 957, 924, 929, 924, 957, 961, 994, 963, 894],
    "literacy Rate": [89.2, 81.51, 87.60, 83.25, 78.44, 93.03, 89.79, 89.56, 91.92, 89.85],
    "famous Place": ["Gateway of India", "Mahalakshmi Temple", "Udgir Fort", 
                           "Ajanta and Ellora Caves", "Tuljapur (Tulja Bhavani Temple)", 
                           "Amba Devi Temple", "Shirdi (Sai Baba)", "Shaniwar Wada", 
                           "Deekshabhoomi", "Trimbakeshwar Temple"],
    "famous_food": ["Vada Pav", "Tambda Rassa", "Local Maharashtrian cuisine", 
                           "Naan Qalia", "Osmanabadi goat mutton", "Local Maharashtrian cuisine", 
                           "Local Maharashtrian dishes", "Misal Pav", "Saoji cuisine", "Misal Pav"],
    "major_crops": ["Not a major hub", "Sugarcane, rice, and jaggery", "Soybean, sugarcane, and pulses", 
                           "Cotton, sorghum, and wheat", "Millet, pulses, and oilseeds", 
                           "Cotton, soybean, and pulses", "Sugarcane, cotton, and millet", 
                           "Not a major hub", "Oranges, cotton, and soybeans", "Grapes, onions, and tomatoes"]
})

class Visualization:
    def __init__(self, data):
        self.data = data

    def population_plots(self, plot_type: str, city_name: str):
        city_data = self.data[self.data['city_name'] == city_name]
        
        if city_data.empty:
            print(f"No data available for {city_name}")
            return
        
        plt.figure(figsize=(10, 6))

        if plot_type == "Barplot":
            sns.barplot(x='city_name', y='population', data=self.data)
            plt.title(f'Population of {city_name}')
            plt.ylabel('Population')
            plt.xlabel('City Name')
        
        elif plot_type == "Scatterplot":
            sns.scatterplot(x='city_name', y='population', data=self.data)
            plt.title(f'Population of {city_name}')
            plt.ylabel('Population')
            plt.xlabel('City Name')

        plt.xticks(rotation=45)
        plt.show()

    def religious_population_plot(self, city_name: str):
        city_data = self.data[self.data['city_name'] == city_name]

        if city_data.empty:
            print(f"No data available for {city_name}")
            return
        
        hindu_population = city_data['hindu_population'].values[0]
        muslim_population = city_data['muslim_population'].values[0]
        other_population = 100 - hindu_population - muslim_population

        population_data = pd.DataFrame({
            'Religion': ['Hindu', 'Muslim', 'Other'],
            'Percentage': [hindu_population, muslim_population, other_population]
        })

        plt.figure(figsize=(10, 6))
        sns.barplot(x='Religion', y='Percentage', data=population_data)
        plt.title(f'Religious Population Distribution in {city_name}')
        plt.ylabel('Percentage')
        plt.xlabel('Religion')
        plt.ylim(0, 100)
        plt.show()




        