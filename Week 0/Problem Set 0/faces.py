def faces():
    input_text = input("Please enter some text containing emoticons :) or :( : ")
    output_text = input_text.replace(":)","🙂").replace(":(","🙁")
    
    print("Output: ",output_text)


if __name__ == '__main__':
    faces()