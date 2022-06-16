if __name__ == "__main__":
    from models import db
    db.truncate()
    with open("id.txt", "w") as fl:
        fl.write("0")
        fl.close()