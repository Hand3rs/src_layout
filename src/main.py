from logzero import logger


def main_func(dummy=314):
    """Just a dumnb function."""
    print("it ran main.")
    test_for_long_line = dummy + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1
    return dummy


if __name__ == "__main__":
    logger.info("TESTTTTTTTTTTT")
    main_func()