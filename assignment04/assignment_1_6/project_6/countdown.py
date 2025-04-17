import time#for time
import sys ##For printing to the same line

def countdown(seconds):
    for i in range(seconds, 0, -1):#countdown
        bar = '█' * (seconds - i) + '-' * (i)
        sys.stdout.write(f"\rCountdown: [{bar}] {i}s remaining")
        #printing countdown
        sys.stdout.flush()
        time.sleep(1)
    sys.stdout.write("\rCountdown: [██████████] 0s remaining\n")
    print("🔔 Time's up!")

def main():
    print("📝 Get ready to type your secret message!")#printed
    time.sleep(1)
    
    user_input = input("Enter your message: ")
    print("\n⏳ Initiating countdown before revealing your message...")#user input
    countdown(10)#countdown
    #printing msg
    print("\n🕵️ Revealing your message in 3...")
    time.sleep(1)
    print("2...")
    time.sleep(1)
    print("1...")
    time.sleep(1)
    print(f"\n💬 Your message was: \"{user_input}\"")#msg printed

if __name__ == '__main__':
    main()
