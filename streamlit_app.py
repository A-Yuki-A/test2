
import streamlit as st

def binary_to_decimal(binary_num):
    decimal_num = int(binary_num, 2)
    return decimal_num

def main():
    st.title("Binary to Decimal Converter")

    binary_input = st.text_input("Enter a binary number:", "1001")
    if st.button("Convert"):
        try:
            decimal_output = binary_to_decimal(binary_input)
            st.success(f"The decimal equivalent is {decimal_output}")
        except ValueError:
            st.error("Please enter a valid binary number.")

if __name__ == "__main__":
    main()

def main():
    st.title("My Streamlit App")
    st.write("Welcome to my first Streamlit app!")

if __name__ == "__main__":
    main()
