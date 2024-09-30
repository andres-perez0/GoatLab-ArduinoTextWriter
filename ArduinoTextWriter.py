import serial
import time

# # serial.Serial('COMXX',baud rate)
ser = serial.Serial(port='COM10',baudrate=115200)
# ser.reset_input_buffer()
# ser.flushInput()

# code from (Python serial port communication using PySerial) https://www.youtube.com/watch?v=Kr1RyK6WENQ&
while True:
    try:
        value=ser.readline()
        valueInString=str(value,'UTF-8')
        print(valueInString)
    except KeyboardInterrupt:
        print("stopped by user")
        break


# with open("arduino_output.txt", "w") as file:
#     while True:
#         try:
#             # Read the data from Arduino
#             if ser.in_waiting > 0:
#                 arduino_output = ser.readline().decode('utf-8').strip()
#                 print(arduino_output)  # Display the output
#                 file.write(arduino_output + "\n")  # Save the output to the text file
#                 file.flush()  # Ensure data is written to the file
#                 time.sleep(1)  # Optional delay to match Arduino output
#         except KeyboardInterrupt:
#             print("Stopped by user")
#             break
