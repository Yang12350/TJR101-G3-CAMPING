# print("Hello everyone! i'm Eta!")

def main():
    for i in range(1,10):
        for j in range(1,10):
            print(f"{i}x{j}={i*j}", end="\t")
        print()

if __name__ == "__main__":
    main()