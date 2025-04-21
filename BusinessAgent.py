from openai import OpenAI

client = OpenAI(api_key='')

def clarity_agent(user_input):
    print("Clarity Agent: Understanding user needs...")
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "user", "content": f"Help me understand how to start making money with my idea: {user_input}"}
        ]
    )
    # Save the response to a text file
    with open("clarity_response.txt", "w") as file:
        file.write(response.choices[0].message.content)
    print("Clarity Agent Response:", response.choices[0].message.content)
    return response.choices[0].message.content

def niche_agent(clarity_response):
    print("Niche Agent: Identifying niche and target avatar...")
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "user", "content": f"Based on this idea: {clarity_response}, help me focus on a specific niche and identify my ideal target avatar."}
        ]
    )
    niche_response = response.choices[0].message.content
    print("Niche Agent Response:", niche_response)
    # Save the response to a text file
    with open("niche_response.txt", "w") as file:
        file.write(niche_response)
    return niche_response

# Example usage
if __name__ == "__main__":
    user_input = input("Enter your business idea: ")
    clarity_response = clarity_agent(user_input)
    niche_agent(clarity_response)
