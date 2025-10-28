# Collaborator Names: (Zanesha Chowdhury - 10440553), (Sabyena Ahmed - 49944985), (Nada El-Fakharany - 50255026)
# Used ChatGPT for syntax, debugging, and pointing out errors. 
# Zanesha wrote functions: load_penguins_csv, my test cases, get_zanesha_calculations,
# Nada wrote functions: largest_bill_length, dream_island_species, get_nada_calculations, my text cases
# Sabyena wrote functions: get_penguin_infos, my test cases, main() functions, get_sabyena_calculations

import unittest
import os
import csv
import math

def load_penguins_csv(f):
    base_path = os.path.abspath(os.path.dirname(__file__))
    full_path = os.path.join(base_path, f)

    with open(full_path, 'r') as file:
        reader = csv.reader(file)
        rows = list(reader)

    # remove the header row
    header = rows[0]
    data = rows[1:]

    return data


# Zanesha's Code Below:
# My part
def avg_body_mass_Adelie(data):
    #Return average body mass (g) for Adelie species, ignoring missing values.
    masses = []
    for row in data:
        species, flipper, body_mass = row
        if species == "Adelie" and body_mass.strip().isdigit():
            masses.append(float(body_mass))
    if len(masses) == 0:
        return 0
    return sum(masses) / len(masses)

def body_mass_flipper_len_corr(data):
    # second function
    # Return correlation between the body mass and the flipper length.
    flippers, masses = [], []
    for row in data:
        species, flipper, body_mass = row
        if flipper.strip().isdigit() and body_mass.strip().isdigit():
            flippers.append(float(flipper))
            masses.append(float(body_mass))

    # Need at least 2 points for correlation
    if len(flippers) < 2:
        return 0

    mean_flipper = sum(flippers) / len(flippers)
    mean_mass = sum(masses) / len(masses)

    num = 0
    for i in range(len(flippers)):
        num += (flippers[i] - mean_flipper) * (masses[i] - mean_mass)
        
    den_x = math.sqrt(sum((f - mean_flipper) ** 2 for f in flippers))
    den_y = math.sqrt(sum((m - mean_mass) ** 2 for m in masses))

    if den_x == 0 or den_y == 0:
        return 0

    return num / (den_x * den_y)

def get_zanesha_calculations(data):
    # Compute both the Adelie average body mass and the flipper length correlation.
    # bigger function
    avg = avg_body_mass_Adelie(data)
    corr = body_mass_flipper_len_corr(data)
    return avg, corr


# Nada's Code Below:

def largest_bill_length(d):
    species_lengths = {}

    for row in d:
        # make sure bill_length_mm is not empty or just spaces
        if row["bill_length_mm"].strip():
            sp = row["species"]
            length = float(row["bill_length_mm"])
            if sp not in species_lengths:
                species_lengths[sp] = []
            species_lengths[sp].append(length)

    avg_lengths = {}
    for sp, values in species_lengths.items():
        avg_lengths[sp] = sum(values) / len(values)

    if avg_lengths:
        largest_species = max(avg_lengths, key=avg_lengths.get)
        largest_value = avg_lengths[largest_species]
    else:
        largest_species = "None"
        largest_value = 0

    return largest_species, largest_value


def dream_island_species(d):
    dream_species = []
    for row in d:
        if row["island"] == "Dream":
            dream_species.append(row["species"])
    if len(dream_species) == 0:
        return "None"
    
    counts = {}
    for sp in dream_species:
        if sp not in counts:
            counts[sp] = 1
        else:
            counts[sp] += 1

    most_common = max(counts, key=counts.get)
    return most_common

def get_nada_calculations(csv_file):
    data = []
    with open(csv_file, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            data.append(row)
    largest_length, _ = largest_bill_length(data)
    dream_species = dream_island_species(data)
    return largest_length, dream_species


# Sabyena's Code Below:
def gentoo_sexes(data):
    
    if isinstance(data, str):  
        with open(data, "r") as f:
            reader = csv.DictReader(f)
            data = list(reader)

    male_count = 0
    female_count = 0

    for row in data:
        if isinstance(row, dict):
            species = row["species"]
            sex = row["sex"]
            year = row["year"]
        else:
            species, sex, year = row

        
        if species == "Gentoo" and year.strip().isdigit():
            if sex == "male":
                male_count += 1
            elif sex == "female":
                female_count += 1

    return {"male": male_count, "female": female_count}


def info_year_chinstrap(data):

    if isinstance(data, str):  
        with open(data, "r") as f:
            reader = csv.DictReader(f)
            data = list(reader)

    chinstrap_year_counts = {}

    for row in data:
        if isinstance(row, dict):
            species = row["species"]
            year = row["year"]
        else:
            species, _, year = row

        if species == "Chinstrap" and year.strip().isdigit():
            y = int(year)
            chinstrap_year_counts[y] = chinstrap_year_counts.get(y, 0) + 1

    if chinstrap_year_counts:
        return max(chinstrap_year_counts, key=chinstrap_year_counts.get)
    else:
        return 0
    
def get_sabyena_calculations(data):
    sexes = gentoo_sexes(data)
    chinstrap_year = info_year_chinstrap(data)
    return sexes, chinstrap_year





# Test Cases

class proj1_test(unittest.TestCase):

    # Zanesha's Test Cases:
    # ChatGPT helped me figure out how to use sample data and decide the edge testcases and explained them to me
    # _ means ignore second value

    # General test cases for 1st func

    def test_avg_body_mass_correct(self):

        # calculates correct average

        sample_data = [["Adelie", "181", "3750"], ["Adelie", "186", "3800"], ["Adelie", "190", "3950"]]
        avg, _ = get_zanesha_calculations(sample_data)
        expected_avg = (3750 + 3800 + 3950) / 3
        self.assertAlmostEqual(avg, expected_avg, places=2)

    def test_avg_body_mass_ignores_missing(self):

        # ignores missing body mass

        sample_data = [["Adelie", "181", "3750"], ["Adelie", "186", ""], ["Adelie", "190", "3950"]]
        avg, _ = get_zanesha_calculations(sample_data)
        expected_avg = (3750 + 3950) / 2
        self.assertAlmostEqual(avg, expected_avg, places=2)

    # Edge test cases for 1st func

    def test_avg_body_mass_single(self):

        # focuses on only one Adelie penguin

        data = [["Adelie", "182", "3800"]]
        avg, _ = get_zanesha_calculations(data)
        self.assertEqual(avg, 3800)

    def test_avg_body_mass_no_adelie(self):

        # no Adelie penguins in dataset

        sample_data = [["Gentoo", "220", "5000"], ["Chinstrap", "210", "4100"]]
        avg, _ = get_zanesha_calculations(sample_data)
        self.assertEqual(avg, 0)
    

    # General test cases for 2nd func
    # _ ignores first value

    def test_corr_positive(self):

        # positive correlation

        data = [["Adelie", "180", "3500"], ["Adelie", "190", "4000"], ["Adelie", "200", "4500"]]
        _, corr = get_zanesha_calculations(data)
        self.assertTrue(0 < corr <= 1)

    def test_corr_ignores_missing(self):

        # ignores rows with missing values

        data = [["Adelie", "180", "3500"], ["Adelie", "", "4000"], ["Adelie", "200", "4500"], ["Adelie", "190", ""]]
        _, corr = get_zanesha_calculations(data)
        self.assertTrue(-1 <= corr <= 1)


    # Edge test cases for 2nd func

    def test_corr_identical_values(self):

        data = [["Adelie", "185", "3800"], ["Adelie", "185", "3800"], ["Adelie", "185", "3800"]]
        _, corr = get_zanesha_calculations(data)
        self.assertEqual(corr, 0)

    def test_corr_single_data_point(self):

        data = [["Adelie", "190", "4000"]]
        _, corr = get_zanesha_calculations(data)
        self.assertEqual(corr, 0)

    # Nada's Test Cases:
    def test_largest_bill_length_1(self):
        data = [
            {"species": "Adelie", "bill_length_mm": "39"},
            {"species": "Gentoo", "bill_length_mm": "47"},
            {"species": "Chinstrap", "bill_length_mm": "45"},
        ]
        species, avg = largest_bill_length(data)                 
        self.assertEqual(species, "Gentoo")

    def test_largest_bill_length_2(self):
        data = [
            {"species": "Adelie", "bill_length_mm": "40"},
            {"species": "Adelie", "bill_length_mm": "42"},
            {"species": "Chinstrap", "bill_length_mm": "46"},
            {"species": "Chinstrap", "bill_length_mm": "48"},
        ]
        species, avg = largest_bill_length(data)               
        self.assertEqual(species, "Chinstrap")

    def test_largest_bill_length_3(self):
        data = []
        species, avg = largest_bill_length(data)
        self.assertEqual(species, "None")

    def test_largest_bill_length_4(self):
        data = [
            {"species": "Adelie", "bill_length_mm": ""},
            {"species": "Gentoo", "bill_length_mm": ""},
        ]
        species, avg = largest_bill_length(data)
        self.assertEqual(species, "None")

    #second function test cases

    def test_dream_island_species_1(self):
        data = [
            {"island": "Dream", "species": "Chinstrap"},
            {"island": "Dream", "species": "Chinstrap"},
            {"island": "Dream", "species": "Gentoo"},
        ]
        result = dream_island_species(data)
        self.assertEqual(result, "Chinstrap")

    def test_dream_island_species_2(self):
        data = [
            {"island": "Dream", "species": "Adelie"},
            {"island": "Dream", "species": "Adelie"},
            {"island": "Dream", "species": "Chinstrap"},
        ]
        result = dream_island_species(data)
        self.assertEqual(result, "Adelie")


    def test_dream_island_species_3(self):
        data = []
        result = dream_island_species(data)
        self.assertEqual(result, "None")

    def test_dream_island_species_4(self):
        data = [
            {"island": "Torgersen", "species": "Adelie"},
            {"island": "Biscoe", "species": "Gentoo"},
        ]
        result = dream_island_species(data)
        self.assertEqual(result, "None")


    




    # Sabyena's Test Cases:
    def test_gentoo_sexes_general1(self):
        sample_data = [
            ["Gentoo", "male", "2007"],
            ["Gentoo", "female", "2008"],
            ["Gentoo", "male", "2009"]
        ]
        result = gentoo_sexes(sample_data)
        expected = {"male": 2, "female": 1}
        self.assertEqual(result, expected)

    # General test case 2:
    def test_gentoo_sexes_general2(self):
        sample_data = [
            ["Adelie", "female", "2007"],
            ["Gentoo", "male", "2008"]
        ]
        result = gentoo_sexes(sample_data)
        expected = {"male": 1, "female": 0}
        self.assertEqual(result, expected)

    # Edge test case 1: 
    def test_gentoo_sexes_edge1(self):
        sample_data = [
            ["Adelie", "male", "2007"],
            ["Chinstrap", "female", "2008"]
        ]
        result = gentoo_sexes(sample_data)
        expected = {"male": 0, "female": 0}
        self.assertEqual(result, expected)

    # Edge test case 2: 
    def test_gentoo_sexes_edge2(self):
        sample_data = [
            ["Gentoo", "", "2007"],
            ["Gentoo", "female", ""]
        ]
        result = gentoo_sexes(sample_data)
        expected = {"male": 0, "female": 0}
        self.assertEqual(result, expected)

    # General test case 1: 
    def test_chinstrap_year_general1(self):
        sample_data = [
            ["Chinstrap", "male", "2007"],
            ["Chinstrap", "female", "2007"],
            ["Chinstrap", "male", "2008"],
            ["Chinstrap", "female", "2007"]
        ]
        result = info_year_chinstrap(sample_data)
        expected = 2007
        self.assertEqual(result, expected)

    # General test case 2: 
    def test_chinstrap_year_general2(self):
        sample_data = [
            ["Chinstrap", "male", "2007"],
            ["Chinstrap", "female", "2008"]
        ]
        result = info_year_chinstrap(sample_data)
        self.assertIn(result, [2007, 2008])

    # Edge test case 1: 
    def test_chinstrap_year_edge1(self):
        sample_data = [
            ["Gentoo", "male", "2007"],
            ["Adelie", "female", "2008"]
        ]
        result = info_year_chinstrap(sample_data)
        expected = 0
        self.assertEqual(result, expected)

    # Edge test case 2: 
    def test_chinstrap_year_edge2(self):
        sample_data = [
            ["Chinstrap", "male", ""],
            ["Chinstrap", "female", " "],
            ["Chinstrap", "male", "abcd"]
        ]
        result = info_year_chinstrap(sample_data)
        expected = 0
        self.assertEqual(result, expected)


def main():
    csv_file = "penguins.csv"

    data = load_penguins_csv(csv_file)

    # Zanesha calculations
    avg, corr = get_zanesha_calculations(data)
    print("Average body mass (Adelie):", round(avg, 2))
    print("Correlation (Body Mass vs Flipper Length):", round(corr, 4))

    # Nada calculations
    largest_length, dream_species = get_nada_calculations(csv_file)
    print("Largest bill length average:", largest_length)
    print("Most prominent species on Dream Island:", dream_species)

    # Sabyena calculations
    gentoo_sexes, info_year_chinstrap = get_sabyena_calculations(csv_file)
    print("Gentoo sexes:", gentoo_sexes)
    print("Most informative year for Chinstraps:", info_year_chinstrap)

    # === Write results to files ===
    with open("zanesha_results.txt", "w") as f:
        f.write(f"Average body mass (Adelie): {avg}\n")
        f.write(f"Correlation (Body Mass vs Flipper Length): {corr}\n")

    with open("nada_results.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Largest bill length average", "Most prominent species on Dream Island"])
        writer.writerow([largest_length, dream_species])

    with open("sabyena_results.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Gentoo males", "Gentoo females", "Most informative Chinstrap year"])
        writer.writerow([gentoo_sexes["male"], gentoo_sexes["female"], info_year_chinstrap])

if __name__ == "__main__":
    unittest.main()