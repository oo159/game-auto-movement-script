"""
before use:
install latest version of python @ python.org
when setting up make sure to (click add to pathway) or else this wont work
then you can click the install no need to custom install
after this is done use idle (comes with python) or a different ide
then last step you have to do is open cmd type "python --version"
if it says python then the version number if not you will have to reinstall AND MAKE SURE TO CLICK ADD TO PATHWAY
after you got the correct output go back into the cmd type "pip install keyboard" (This will allow to get keyboard inputs/outputs)
After you install keyboard run the command "pip3 install pyautogui" (this will allow for mouse inputs/outputs)
(the time import should auto be installed with python)
you are finaly done, you can click run and have op movement
script by BetterBrowse~
"""
import keyboard
import pyautogui
import time
def main():
    disclaimer()
    getSelectedUserInputs()
def diclaimer():
    print("We are not responsible for account bans")
    print("The players that use this script")
    print("The way it affects the game, game company, and platform")
    print("And any possible hardware damage")
def getSelectedUserInputs():
    userforward = input("What key do you have selected for moving forward: ")
    userJump = input("What key do you have selected for jumping: ")
    if userJump == " ":
        print("SPACE")
    userCrouch = input("What key do you have set for crouching (if CTRL spell CTRL): ")
    autoRunKey = input("What key do you want for auto walk/run: ")
    autoJumpKey = input("What key do you want for auto jump: ")
    autoCrouchKey = input("What key do you want for auto crouch: ")
    endAllActionsKey = input("what key do you want selected for to end all current automations: ")
    keyDectionAndOutput( userforward, userJump, userCrouch, autoRunKey, autoJumpKey, autoCrouchKey, endAllActionsKey)
def keyDectionAndOutput (forw, jump, crouch, auto1, auto2, auto3, end):
    autoWalk = 0
    autoJump = 0
    autoCrouch = 0
    errorCount = 0
    totalError = 0
    while True:
        if errorCount % 2 == 0 and errorCount != 0:
            autoWalk-=1
            autoJump-=1
            autoCrouch-=1
            keyboard.press("ESC")
            keyboard.release("ESC")
            time.sleep(.1)
            keyboard.press("ESC")
            keyboard.release("ESC")
            errorCount-=2
        if keyboard.is_pressed(end):
            if autoWalk == 1:
                autoWalk-=1
            if autoJump == 1:
                autoJump-=1
            if autoCrouch == 1:
                autoCrouch-=1
            if autoWalk == 0 and autoJump ==  0 and autoCrouch == 0:
                keyboard.press("ESC")
                keyboard.release("ESC")
                time.sleep(.1)
                keyboard.press("ESC")
                keyboard.release("ESC")
            else:
                print("error count: " + totalError)
                print("error shutting off automations")
                print("next error autoreset")
                errorCount+=1
                totalError+=1
        if autoWalk == 1:
            pyautogui.keyDown(forw)
        if autoJump == 1:
            keyboard.press(jump)
            keyboard.release(jump)
            time.sleep(1)
        if autoCrouch == 1:
            keyboard.press(crouch)
            keyboard.release(crouch)
            time.sleep(.250)
        if keyboard.is_pressed(auto1):
            if autoWalk == 0:
                autoWalk+=1
            else:
                autoWalk-=1
                keyboard.press("ESC")
                keyboard.release("ESC")
                time.sleep(.1)
                keyboard.press("ESC")
                keyboard.release("ESC")
        if keyboard.is_pressed(auto2):
            if autoJump == 0:
                autoJump+=1
            else:
                autoJump-=1
        if keyboard.is_pressed(auto3):
            if autoCrouch == 0:
                autoCrouch+=1
            else:
                autoCrouch-=1
        time.sleep(.12)
main()

