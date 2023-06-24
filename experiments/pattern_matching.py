import re
text = '''
response: Here is the updated table:

[['ID:', 'FR1'], 
['Title:', 'Turn ON the device'], 
['Description:', 'To turn ON the laser pen, the user presses and holds the first button (labelled as ON/OFF button – bottom of the pen) until the LED turns green.'], 
['Depth:', 'None'], 
['Edge Cases', ''], 
['Error Handling', ''], 
['How to respond in abnormal situations', 'For example, "If the LED fails to turn green when the device is turned on, the software should alert the user with a specific error message or sound."'], 
['ID:', 'FR2'], 
['Title:', 'Activate the protocol n°1'], 
['Description:', 'The user press once the second button (on the top of the pen) and the LED light turns Blue.\nLaser output last for 10 seconds then the Blue LED Light turns off.'], 
['Depth:', 'FR1'], 
['Edge Cases', ''], 
['Error Handling', ''], 
['How to respond in abnormal situations', 'For example, "If the LED fails to turn green when the device is turned on, the software should alert the user with a specific error message or sound."], 
['ID:', 'FR3'], 
['Title:', 'Activate the protocol n°2'], 
['Description:', 'The user presses twice the second button (on the top of the pen) and the LED light turns Purple.\nLaser output last for 20 seconds then the Purple LED Light turns off.'], 
['Depth:', 'FR1'], 
['Edge Cases', ''], 
['Error Handling', ''], 
['How to respond in abnormal situations', 'For example, "If the LED fails to turn green when the device is turned on, the software should alert the user with a specific error message or sound."], 
['ID:', 'FR4'], 
['Title:', 'Turn OFF the device'], 
['Description:', 'To turn OFF the laser pen, the user presses and holds the first button (labelled as ON/OFF button - bottom of the pen) until the green LED disappears.'], 
['Depth:', 'FR1'], 
['Edge Cases', ''], 
['Error Handling', ''], 
['How to respond in abnormal situations', 'For example, "If the LED fails to turn green when the device is turned on, the software should alert the user with a specific error message or sound."], 
['ID:', 'FR5'], 
['Title:', 'Shutdown time after inactivity'], 
['Description:', 'After not using the laser pen for 5 minutes, the device switches off.'], 
['Depth:', 'FR1'], 
['Edge Cases', ''], 
['Error Handling', ''], 
['How to respond in abnormal situations', 'For example, "If the LED fails to turn green when the device is turned on, the software should alert the user with a specific error message or sound."],
['ID:', 'FR6'], 
['Title:', 'Safety Requirements'], 
['Description:', 'The software shall be designed to ensure the safety of the user during the use of the device.'], 
['Depth:', 'None'], 
['Edge Cases', ''], 
['Error Handling', ''], 
['How to respond in abnormal situations', 'For example, "If the device detects any abnormality during use, it should immediately stop the laser output and alert the user with a specific error message or sound."]]
'''

pattern = r"response:.*?\[\[(.*)"

match = re.search(pattern, text)
if match:
    extracted_text = match.group(1).strip()
    print(extracted_text)

