import runner
import schedule


def test():    
    runner.run()
    print("Ran at: " + str(datetime.datetime.now()))

if __name__ == "__main__":
    schedule.every(1).minutes.do(test)
    #schedule.every().hour.do(test)
    #schedule.every().day.at("10:30").do(test)
    #schedule.every().monday.do(test)
    #schedule.every().wednesday.at("13:15").do(test)
    
    while True:
        schedule.run_pending()
        time.sleep(1)