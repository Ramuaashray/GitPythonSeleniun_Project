from PageObjects.file_download_update import file_download_update


def test_upload_file_validtion(browserInstance):

    driver = browserInstance
    driver.get("https://rahulshettyacademy.com/upload-download-test/index.html")
    file_download_up = file_download_update(driver)
    file_download_up.download_file()
    file_download_up.update_file()
    file_vali = file_download_up.upload_file()
    file_vali.file_validation()





