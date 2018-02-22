'''
Initial code for encouraging dialogue with Baymax

Vicky McDermott
2/21/2018
'''

def intro():
    print("Hello, I am Baymax, your personal health care companion, what seems to be the problem?")
    print("(sad, happy, pain)")
    problem = input()
    if problem == 'sad':
        sad()
    elif problem == 'happy':
        happy()
    elif problem == 'pain':
        pain()

def baymax_help():
    print("How can I help you?")
    print("(sad, happy, pain)")
    problem = input()
    if problem == 'sad':
        sad()
    elif problem == 'happy':
        happy()
    elif problem == 'pain':
        pain()

def pain():
    print("On a scale of 1 to 10, how would you rate your pain?")
    rating = input()
    print(rating)

def sad():
    print("Don't be sad be happy!")

def happy():
    print("Yay! Fist bump! Bada-lada-la!")

def ending():
    print("Are you satisfied with your care? (yes or no)")
    answer = input()
    return answer

if __name__ == '__main__':
    intro()
    end = ending()
    while(end != 'yes'):
        baymax_help()
        end = ending()
