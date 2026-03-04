from art import logo
print(logo)

training_data = [
    {
        "category" : "Image Recognition",
        "total_samples" : 500,
        "accuracy_score" : 0.82,
        "tags" : ["cnn","deep-learning","vision"]
    },
    {
        "category": "Text",
        "total_samples": 400,
        "accuracy_score": 0.95,
        "tags": ["cnn2", "deep-learning2","vision2"]

    },
]
def add_new_dataset(category_value,total_samples_value,accuracy_score_value,tags_value):
    new_dictionary = {
        "category" : category_value,
        "total_samples" : total_samples_value,
        "accuracy_score": accuracy_score_value,
        "tags" :tags_value,
    }
    training_data.append(new_dictionary)

def show_best_model():
    for find_highest in training_data:
        if find_highest["accuracy_score"] > 0.90:
            print(find_highest["category"])

continue_to_add = True
while continue_to_add:
    category_to_add = input("Category add: ")
    total_samples_to_add = int(input("Total samples add: "))
    accuracy_score_to_add = float(input("Accuracy score add: "))
    tags_add_list = []
    tags_amount = int(input("How many tags to add? :"))
    for tags_add in range(tags_amount):
        tags_to_add = input("Tags add: ")
        tags_add_list.append(tags_to_add)
    add_new_dataset(category_value=category_to_add, total_samples_value=total_samples_to_add,
                    accuracy_score_value=accuracy_score_to_add, tags_value=tags_add_list)
    should_continue = input("Do you want to add continue,Type 'yes' or 'no'").lower()
    if should_continue == "yes":
        print("\n" * 5)
    elif should_continue == "no":
        continue_to_add = False
        show_best_model()