import sys
import selenium, selenium.webdriver

if (len(sys.argv) < 3):
    print("Usage: python LinkVisitor.py <link> <number_of_iterations>")
    sys.exit(1)

link = sys.argv[1]
x = int(sys.argv[2])

driver = selenium.webdriver.Firefox()
driver.get(link)

for i in range(x):
    # TODO: change ip through vpn
    driver.refresh()

driver.quit()