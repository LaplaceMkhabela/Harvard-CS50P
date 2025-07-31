def playback():
    input_text = input("Please enter some text: ")
    output_text = input_text.replace(" ","...")
    print("Output: ",output_text)



if __name__ == '__main__':
    playback()