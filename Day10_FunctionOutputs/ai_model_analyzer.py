from ai_models import ai_models_dictionary


def format_name(name):
    formated_model_name = name.replace('_',' ').title()
    return f"Model: {formated_model_name}"


def get_analysis_report(accuracy,latency):
    model_status = ""
    if  accuracy > 0.90 and latency < 50:
        model_status = "Elite model"
    else:
        model_status = "Standard model"

    return f"Status: {model_status}"



for models in ai_models_dictionary:
    formated_name = format_name(models["model_name"])
    report = get_analysis_report(accuracy=models["accuracy_score"],
                                 latency=models["latency_ms"])

    print(f"{formated_name} | {report}")



