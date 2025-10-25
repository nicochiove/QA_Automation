def test_successful_login(loginWithDriver):
    
    try:
        driver = loginWithDriver

        assert '/inventory.html' in driver.current_url, "No se logro la redirección correcta"
    
    except Exception as e:
        print(f"Error en test_successful_login: {e}")
        raise
    finally:
        driver.quit()

