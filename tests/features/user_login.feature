Feature: User login

    Scenario: Logged in
        Given that the user is on the page "http://localhost:5000/auth/login"
        When you insert the "email" "larry12@gmail.com"
        And insert the "password" "matheuslindao"
        Then click the button "Sign in"
        And the message should be displayed
            """
                Larry, seu login foi realizado com sucesso.
            """

    Scenario: Invalid email
        Given that the user is on the page "http://localhost:5000/auth/login"
        When you insert the "email" "larry95@gmail.com"
        And insert the "password" "matheuslindao"
        Then click the button "Sign in"
        And the message should be displayed
            """
                Ooops, o email está incorreto. Tente novamente.
            """

    Scenario: Invalid password
        Given that the user is on the page "http://localhost:5000/auth/login"
        When you insert the "email" "larry12@gmail.com"
        And insert the "password" "matheuslindao"
        Then click the button "Sign in"
        And the message should be displayed
            """
                Ooops, a senha está incorreta. Tente novamente;
            """


    Scenario: User not registered
        Given that the user is on the page "http://localhost:5000/auth/login"
        When you insert the "email" "baesse23@hotmail.com"
        And insert the "password" "linuxevida"
        Then click the button "Sign in"
        And the message should be displayed
            """
                Ooops, esse usuário não está cadastrado no sistema.
            """