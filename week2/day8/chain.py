import os
from pathlib import Path
from urllib import response
from dotenv import load_dotenv
from groq import Groq
import re
from time import sleep

load_dotenv()

my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("api error")

client = Groq(api_key=my_api_key)
model = "qwen/qwen3.8-27b"


JD = """
Catallaxy is looking for a talented full-stack developer (node.js) able to quickly develop, deliver and support clean, scalable and high quality code for blockchain applications.

You will work closely with the head of product
You will have the opportunity to grow inside the organization
Job Location: Montreal, Quebec, Canada

Job type: Full time

Responsibilities:

Design, develop, deliver, and support web-based applications and APIs
Write maintainable code with extensive tests and version control
Ensure the scalability and quality of all code and products
Build applications that focus on great user experience
Create automated testing to quickly and confidently ship code
Assist with product documentation, unit testing and ensuring overall product quality
Participation in daily scrums, design discussions, code reviews and code analysis
Help choose and define the tech stack and tools
Requirements

3+ years experience in software development
2+ years with JavaScript technologies: Node.js and React/Angular or similar
Experience building scalable web applications using modern frameworks (React/ Angular, etc.) and tools (npm, webpack, etc.)
Good understanding of both front end (JavaScript, HTML, CSS) and server side (Node.js, express) components
Experience with API design and development (REST, JSON, RESTFull services).
CSS preprocessors like Sass or LESS
Front-end (CSS) frameworks like Foundation or Bootstrap
JS-based build tools like Grunt, Gulp, and Bower
Experience using test-driven development and writing accurate tests
Experience with databases SQL and NoSQL (MongoDB, Postgres, etc...)
Ability to translate technical requirements into elegant code solutions
Focus on continuous improvement
Experience with cloud providers (AWS/OVH/Google, etc.) and service deployment
Embrace Agile/Scrum methodologies and development best practices
Experience with Git
Keeping in mind Security concerns throughout the process
Excellent problem solving and debugging skills to rapidly identify and fix bugs and problems
Ability to identify, implement and manage code libraries that minimize repetitive code and improve application design
Use code optimization techniques to improve robustness and performance of software
Human skills:

Proven and strong communication skills (in English and/or French)
Team player, but also fully able to efficiently accomplish tasks independently
Strong analytical and problem solving skills
You get things done
Willingness to wear multiple hats and be flexible in a fast-moving environment
Nice to have

Bachelor or master degree in Computer Science, a related field or equivalent experience
Knowledge/experience with other programing languages (C++, Go, .Net, Python)
Blockchain, bitcoin interest or willing to learn
Interest in smart contract (Ethereum)
Mobile dev (IOS, Android) or ability to hire and manage someone if needed
Experience with distributed systems and decentralized technologies
Experience with message or event driven architectures (such as RabbitMQ or Kafka)
Continuous Integration (CI) and Continuous Delivery (CD) DevOps experience.
Experience with Docker
Knowledge of Micro Services concepts and architecture
Please submit a resume, and a short text highlighting your experience with the mentioned programing languages and tools as well as your experience developing web applications and products.

About Catallaxy

With more than 15 Montreal-based experts and nearly 50 strategic partners worldwide, our service offering combines the technical expertise of the best core Blockchain talents and the strategic consulting power of Raymond Chabot Grant Thornton. Our objective is to prepare businesses for their blockchain transformation.

Catallaxy is also launching the Blockhouse. The Blockhouse is a unique innovation center bringing together the most influential players in the blockchain community. Strategically based in Montréal, the Blockhouse is a unique international showcase for decentralized and distributed technologies.
"""
RESUME = """
Ayush Arya
SUMMARY OF QUALIFICATION
• Senior Full Stack Developer with 7+ years of experience specializing in designing scalable microservices, cloud architecture(AWS/GCP), and high performance applications. Proven track record of transitioning monolithic to modular, domain driven system architecture.
• Highly motivated with superior analytical, organizational, communicational skills and quick learner.
EDUCATION
Concordia University
Masters in Software Engineering, May 2020
University of Delhi
Bachelor of computer science Graduated: Jun 2017
SKILLS
Programming
•JavaScript •Typescript •C++ •Java •Node.js •GraphQL •AJAX •MongoDB •SQL •PostgreSQL •HTML5 •CSS3.
Libraries and Framework
•React.js •React native •Redux.js •Express.js •JQuery •Bootstrap •Handlebars.js •Redux Saga •Socket.io •Fastify Miscellaneous
•Aws lambda •Step function •SQS •SNS •API Gateway • DynamoDb •EventBridge •Kinesis •Athena •S3 •IAM •Kubernetes •Helm Charts •Apollo •Neo4j •Git •OOPS •Redis •Docker •DataDog •Sentry •JSON •CircleCI •OAuth2.0 •TDD •Heroku •Rest APIs •Jenkins •LaunchDarkly •SonarQube •Jira •Postman •GCP •ESLint •Confluence •LucidChart •Claude •Cursor •Gemini
Soft Skills
•Teamwork • Leadership
EXTRAS
2017 Vice President
Association of Computer Enthusiasts
2016 General Secretary Association of Computer Enthusiasts 2014 Volunteer
University Placement Cell
AWARDS
University of Delhi
2017 Student of the year 2017 Best Paper Presentation
WORK EXPERIENCE
Senior Software Developer | ParagonERP (May,25, Present)
● Architected and built core platform libraries(IAM, logging, error-handling) adopted across 15+ microservices, improving consistency, security, and developer efficiency by reducing boilerplate code by 30% and accelerating feature delivery time across engineering teams.
● Architected and delivered domain-driven microservices(User, Product, Inventory) enabling the platform to shift from monolith to modular, customer configurable product offerings.
● Elevated engineering quality by implementing SonarQube and Opentelemetry, driving standards, leading code reviews, mentoring peers, and shaping architectural and design decisions.
● Technologies: Typescript, Nodejs, PostgreSQL, RabbitMQ, Redis, Ory Hydra, React, Redux, Docker, Kubernetes, GCP, Hexagonal architecture, domain-driven design etc.
Software Developer 3 | SSENSE (Oct,22– May,25)
• • • • •
Engineered and scaled high-throughput inventory service supporting stock transfers, warehouse tracking, and fulfillment operations.
Architected serverless workflows using AWS Step Functions and EventBridge, achieving 99.9% reliability for automated inventory sync processes.
Designed and Presented BPMN architecture diagrams, implementing AWS infrastructure using cloud formation.
Wrote testable, efficient and reusable code majorly in Typescript suitable for CI/CD, that respected best practices and development standards.
Technologies: AWS lambda, Step function, SQS, SNS, S3, API Gateway, Event Bridge, Kinesis, DynamoDb, Nodejs, Typescript, Inversify, Dependency injection, Datadog, Jest, React, Redux, Okta, Lucidcharts, Launchdarkly, Dockers, Jira, GitHub.
Full stack developer & Software Engineer | Sentiance & Aaqua (Jun,20– Sep,22)
• Developed a scalable social media mobile application with an administrative web dashboard. Created executors i.e., cypher queries to access the graph database and resolvers i.e., GraphQL API to communicate between Java services, Database and Front- end. Worked on creating chat application from scratch using sendbird and getStream chat provider. Translated UI designs from Figma to code, maintained 100% test coverage and end-to-end testing.
• Technologies: React-native, React, Redux, Typescript, NodeJS, Koa, Apollo GraphQL Client & Server, Neo4j, Sentry, Nx, Jest, Storybook, Detox, Cucumber, Figma, Sentry, Dockers, Bitbucket, Git, CSS & styled components.
• Participated in daily standups and bi-weekly ceremonies (Agile), performing daily cross-team code reviews and working 100% remotely in international team.
Full stack developer | Definitechs Inc. District 3, Montreal, Canada (Mar–Jun,19)
• Designed, developed and deployed the backend and frontend of the product. Collaborated with AI developer to design and develop services required for up and running the company’s AI Engine on cloud. Technologies: Node.js, MongoDB, React.js, Redux, Docker, AWS etc. Designed and coded application components in an Agile environment by sharing knowledge with and mentoring team members in the areas of expertise.
Full stack developer | Coding Ninjas, New Delhi, India(Feb,2017– July, 2018)
• Developed and maintained front-end using React.js components, Forms, Events, Router and Redux. Worked on Back-end using Node.js, Express.js and MongoDB. Created Rest APIs for interaction between server and client and used OAuth 2.0 service.

"""


def ask_llm(system_prompt, user_prompt):
    sys_msg = {"role": "system", "content": system_prompt}
    user_msg = {"role": "user", "content": user_prompt}

    messages = [sys_msg, user_msg]
    response = client.chat.completions.create(model=model, messages=messages)
    answer = response.choices[0].message.content
    return answer


def step1_res_extraction(RESUME):
    # extract skills from resume
    system_prompt = """
    you are a professional HR assistant. extract the skills from the candidates resume provided.
    Only return the skills no other information. Do not invent any skills by yourself.
    """

    user_prompt = f"""
    Extract the skills from this resume
    {RESUME}
    """

    return ask_llm(system_prompt, user_prompt)


def step2_JD_extraction(JD):
    # extract skills from resume
    system_prompt = """
    you are a professional HR assistant. extract the skills from the Job Description provided.
    Only return the skills no other information. Do not invent any skills by yourself.
    """

    user_prompt = f"""
    Extract the skills from this Job description
    {JD}
    """

    return ask_llm(system_prompt, user_prompt)


def step3_match(candidate, jd):
    system_prompt = """
    you are a professional HR assistant. compare the skills of candidate and the skills required in the JD and produce a final score between 1 and 100.
    also produce a short verdicr whether the candidate is a good fit for the role
    """
    user_prompt = f"""
    Compare and match the skills
    JD:
    {JD}
    Candidate:
    {candidate}
    """
    return ask_llm(system_prompt, user_prompt)


candidate = step1_res_extraction(RESUME)
print(candidate)
sleep(2)
jd = step2_JD_extraction(JD)
sleep(2)
score = step3_match(candidate, jd)
print(score)
