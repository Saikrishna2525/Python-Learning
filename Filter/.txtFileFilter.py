documents = ["data.csv", "notes.txt", "report.pdf"]
print(list(filter(lambda x: str(x).endswith(".txt"), documents)))
