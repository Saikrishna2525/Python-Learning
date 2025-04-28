def personalized_Greeting(*name, **greets):
    greet = greets.get("greeting", "Hello")
    for i in name:
        print(f"{greet}, {i}!")
