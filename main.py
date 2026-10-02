import requests
import html

def run_trivia_quiz():
    # URL fetches 5 multiple-choice questions across random categories
    url = "https://opentdb.com"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error connection failed: {e}")
        return

    if data.get("response_code") != 0:
        print("Could not retrieve quiz questions at this time.")
        return

    questions = data.get("results", [])
    score = 0

    print("--- Project 2: Interactive Trivia Quiz ---")
    
    for index, q in enumerate(questions, 1):
        # Decode HTML entities (e.g., &quot; to ") from the API response
        category = html.unescape(q["category"])
        question_text = html.unescape(q["question"])
        correct_answer = html.unescape(q["correct_answer"])
        incorrect_answers = [html.unescape(ans) for ans in q["incorrect_answers"]]
        
        # Combine and sort choices so the correct answer isn't always last
        options = sorted(incorrect_answers + [correct_answer])
        
        print(f"\nQuestion {index} | Category: {category}")
        print(question_text)
        
        for idx, option in enumerate(options, 1):
            print(f"  {idx}. {option}")
            
        # Get and validate user input
        while True:
            try:
                user_choice = int(input("Your answer (1-4): "))
                if 1 <= user_choice <= 4:
                    break
                print("Please enter a number between 1 and 4.")
            except ValueError:
                print("Invalid input. Please enter a number.")
                
        # Check answer
        selected_answer = options[user_choice - 1]
        if selected_answer == correct_answer:
            print("✨ Correct!")
            score += 1
        else:
            print(f"❌ Wrong. The correct answer was: {correct_answer}")

    print(f"\n🏁 Quiz Completed! Your final score: {score}/{len(questions)}")

if __name__ == "__main__":
    run_trivia_quiz()
