import operations
import logging

logging.basicConfig(
    level=logging.DEBUG,
    filemode="w",
    filename="test.log"
    
)

if __name__ == "__main__":

    ##logging.info('Test case 1')

    ##result = operations.add(1,2)

    ##if result == 3:
      ##  logging.info("PASS")

   ## else :
     ##   logging.info("FAIL")

    logging.info('Test case 3')
    result = operations.power(2,3)
    if result == 1:
        logging.info("PASS")
    else :
        logging.info("FAIL")


    ##result = operations.add(3,2)
    logging.info(f"Result= {result}")

    logging.warning("Division endiablada")
    logging.error('Error')
    logging.debug('The value in a and b is ...')
    logging.critical('Critical in time')