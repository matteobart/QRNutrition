import json
import argparse

#does not check for notes
#only checks v1
#does not check for all nutrients

def check_attribute(data, lst, name, typ):
	if data.get(name) == None:
		lst.append("Missing " + str(name) + " attribute")
		return True
	if not isinstance(data.get(name), typ):
		lst.append("Incorrect type for " + str(name) + " attribute") 
		return True
	return False

def check_ingredient(item, lst):
	if not isinstance(item, str):
		lst.append("Ingredient", item, "is not the right type")
		return True
	return False

def check_top_level(data, lst):
	top_levels = ["v", "name", "company", "nutrition", "ingredients", "kosher", "vegan", "vegetarian", "gluten_free", "fair_trade", "notes"]
	for level in data.keys():
		if level not in top_levels:
			lst.append(level, "should not be in the top level (consider putting it in 'notes')")


# will return a list of strings that are the errors for a given json
def check_json(filename):
	ret = []
	file = open(filename, "r")
	json_data = json.load(file)
	check_attribute(json_data, ret, "name", str) 
	check_attribute(json_data, ret, "company", str)
	if not check_attribute(json_data, ret, "nutrition", dict):
		nutrition_dict = json_data["nutrition"]
		check_attribute(nutrition_dict, ret, "servings", str) 
		check_attribute(nutrition_dict, ret, "serving_size", str) 
		check_attribute(nutrition_dict, ret, "serving_size_grams", str) 
		check_attribute(nutrition_dict, ret, "total_fat", str) 
		check_attribute(nutrition_dict, ret, "total_fat_dv", str) 
		check_attribute(nutrition_dict, ret, "sat_fat", str) 
		check_attribute(nutrition_dict, ret, "sat_fat_dv", str) 
		check_attribute(nutrition_dict, ret, "trans_fat", str) 
		check_attribute(nutrition_dict, ret, "cholesterol", str) 
		check_attribute(nutrition_dict, ret, "cholesterol_dv", str) 
		check_attribute(nutrition_dict, ret, "sodium", str) 
		check_attribute(nutrition_dict, ret, "sodium_dv", str) 
		check_attribute(nutrition_dict, ret, "total_carbohydrates", str) 
		check_attribute(nutrition_dict, ret, "total_carbohydrates_dv", str) 
		check_attribute(nutrition_dict, ret, "fiber", str) 
		check_attribute(nutrition_dict, ret, "fiber_dv", str) 
		check_attribute(nutrition_dict, ret, "total_sugars", str) 
		check_attribute(nutrition_dict, ret, "added_sugars", str) 
		check_attribute(nutrition_dict, ret, "added_sugars_dv", str) 
		check_attribute(nutrition_dict, ret, "protein", str) 
		check_attribute(nutrition_dict, ret, "vitamin_d_dv", str) 
		check_attribute(nutrition_dict, ret, "calcium_dv", str) 
		check_attribute(nutrition_dict, ret, "iron_dv", str) 
		check_attribute(nutrition_dict, ret, "potassium_dv", str) 
	if not check_attribute(json_data, ret, "ingredients", list):
		ingredients_list = json_data["ingredients"]
		for item in ingredients_list:
			check_ingredient(item, ret)
	check_attribute(json_data, ret, "kosher", bool)
	check_attribute(json_data, ret, "vegan", bool)
	check_attribute(json_data, ret, "vegetarian", bool)
	check_attribute(json_data, ret, "gluten_free", bool)
	check_attribute(json_data, ret, "fair_trade", bool)
	check_top_level(json_data, ret)
	return ret
	
	
if __name__ == "__main__":
	# do some arg checking
	parser = argparse.ArgumentParser(description='Check a JSON to see if it is a valid nutrition label')
	parser.add_argument('filename', type=str, help='Input to check')
	args = parser.parse_args()
	val = check_json(args.filename)
	if val == []:
		print("File:", args.filename, "LGTM")
	else:
		print("File:", args.filename, "errors")
		print(*val, sep="\n")