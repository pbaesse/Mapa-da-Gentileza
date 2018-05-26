Feature: Add post

    Scenario: Post successfully added
        Given that the user is on the page "http://localhost:5000/feed"
        When you click the button "newPost"
        <!-- Ver como vai ser essa funcionalidade para criar o cenário -->
        And insert the "title"

