def einstein():
    C = 300000000  #speed of light 300 000 000 m/s
    mass = input("Please enter the mass(in kg): ")
    E = int(mass) * C**2

    print(f"Energy (joules): {E}")


if __name__ == "__main__":
    einstein()