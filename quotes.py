# -*- coding: utf-8 -*-
import random
import datetime, discord, os, dotenv, asyncio, calendar

intents = discord.Intents().all()
intents.members= True

client = discord.Client(intents=intents)
TOKEN = "MTA5NjgwNjUzMTA5MTE1Mjk3OQ.GISh4_.nKlucH4amNg_qH6vN3X93ok1svTox0BOIJIZZE"

# Add your quotes for each day of the week
quote_lists = {
    0: ["“Bet on me? Bet I will.” — Lizzo",
            "“Before anything else, preparation is the key to success.” — Alexander Graham Bell",
            "“Stay afraid, but do it anyway. What's important is the action. You don’t have to wait to be confident. Just do it and eventually the confidence will follow.” — Carrie Fisher",
            "“Make each day your masterpiece.” — John Wooden",
            "“Your talent determines what you can do. Your motivation determines how much you’re willing to do. Your attitude determines how well you do it.” — Lou Holtz",
            "“I learned this, at least, by my experiment; that if one advances confidently in the direction of his dreams, and endeavors to live the life which he has imagined, he will meet with a success unexpected in common hours.” — Henry David Thoreau",
            "“​​We will fail when we fail to try.” — Rosa Parks",
            "“Don’t count the days, make the days count.” — Muhammad Ali",
            "“I love to see a young girl go out and grab the world by the lapels. Life’s a bitch. You’ve got to go out and kick ass.” — Maya Angelou",
            "“Without ambition one starts nothing. Without work one finishes nothing. The prize will not be sent to you. You have to win it.” — Ralph Waldo Emerson",
            "“You’ve got to get up every morning with determination if you’re going to go to bed with satisfaction.” — George Lorimer",
            "“Boss up and change your life / You can have it all, no sacrifice” — Lizzo",
            "“The plan is to fan this spark into a flame.” — Lin-Manuel Miranda"],
    1: ["“Real change, enduring change, happens one step at a time.“ — Ruth Bader Ginsburg",
    "“Light tomorrow with today.“ — Elizabeth Barrett Browning",
    "“Drench yourself in words unspoken / Live your life with arms wide open / Today is where your book begins / The rest is still unwritten“ — Natasha Bedingfield",
    "“And now that you don’t have to be perfect, you can be good.“ — John Steinbeck",
    "“Never give up on a dream just because of the time it will take to accomplish it. The time will pass anyway.“ — Earl Nightingale",
   "“Someday is not a day of the week.“ — Janet Dailey",
    "“‘Today is always here,’ said Sethe. ‘Tomorrow, never.’ ― Toni Morrison",
    "“Too late for second-guessing / Too late to go back to sleep / It’s time to trust my instincts / Close my eyes and leap.“ — Stephen Schwartz",
    "“A year from now you may wish you had started today.“ — Karen Lamb",
    "“Try not. Do, or do not. There is no try.“ — Yoda",
    "“People talk about confidence without ever bringing up hard work. That’s a mistake. I know I sound like some dour older spinster on Downton Abbey who has never felt a man’s touch and whose heart has turned to stone, but I don’t understand how you could have self-confidence if you don’t do the work… Because confidence is like respect; you have to earn it.“ — Mindy Kaling",
    "“Real courage is when you know you’re licked before you begin, but you begin anyway and see it through no matter what.“ ― Harper Lee",
    "“You get to decide where your time goes. You can either spend it moving forward, or you can spend it putting out fires. You decide. And if you don’t decide, others will decide for you.“ — Tony Morgan",
    "“Don’t sit down and wait for the opportunities to come. Get up and make them.“ — Madam C.J Walker",
    "“The key is not to prioritize what’s on your schedule, but to schedule your priorities.“ — Stephen Covey",
    "“Imagining something may be the first step in making it happen, but it takes the real time and real efforts of real people to learn things, make things, turn thoughts into deeds or visions into inventions.“ — Mr. Rogers"
],
    2: ["“When someone tells me ‘no,’ it doesn’t mean I can’t do it, it simply means I can’t do it with them.” — Karen E. Quinones Miller",
            "“What we fear of doing most is usually what we most need to do.” — Ralph Waldo Emerson",
            "“You may not control all the events that happen to you, but you can decide not to be reduced by them.” — Maya Angelou",
            "“Believe you can and you’re halfway there.” — Theodore Roosevelt",
            "“There will always be hurdles in life, but if you want to achieve a goal, you must continue.” — Malala Yousafzai",
            "“Remember to look up at the stars and not down at your feet. Try to make sense of what you see and wonder about what makes the universe exist. Be curious. And however difficult life may seem, there is always something you can do and succeed at. It matters that you don't just give up.” ― Stephen Hawking",
            "“The most important step a man can take. It's not the first one, is it? It's the next one. Always the next step.” ― Brandon Sanderson",
            "“Even if you’re on the right track, you’ll get run over if you just sit there.” — Will Rogers",
            "“There will be people who say to you, ‘You are out of your lane.’ They are burdened by only having the capacity to see what has always been instead of what can be. But don’t you let that burden you.” — Kamala Harris",
            "“Never confuse a single defeat with a final defeat.” — F. Scott Fitzgerald",
            "“I’m a survivor / I’m not gonna give up / I’m not gonna stop / I’m gonna work harder” — Destiny’s Child",
            "“Never allow a person to tell you no who doesn’t have the power to say yes.” — Eleanor Roosevelt",
            "“Only when we're drowning do we understand how fierce our feet can kick.” ― Amanda Gorman",
            "“Real courage is holding on to a still voice in your head that says, ‘I must keep going.’ It’s that voice that says nothing is a failure if it is not final. That voice that says to you, ‘Get out of bed. Keep going. I will not quit.’” — Cory Booker",
            "“I break chains all by myself / Won’t let my freedom rot in hell / Hey! I’ma keep running / ‘Cause a winner don't quit on themselves” — Beyoncé"],
    3: ["“Your imagination is your preview of life’s coming attractions.” — Albert Einstein",    "“If you don’t design your own life plan, chances are you’ll fall into someone else’s plan and guess what they have planned for you? Not much.” — Jim Rohn",    "“You can’t make decisions based on fear and the possibility of what might happen.” — Michelle Obama",    "“It is better to fail in originality than to succeed in imitation.” — Herman Melville",    "“Do not stop thinking of life as an adventure. You have no security unless you can live bravely, excitingly, imaginatively; unless you can choose a challenge instead of competence.” ― Eleanor Roosevelt",    "“Do not let anyone ever tell you who you are.” — Kamala Harris",    "“You can get what you want or you can just get old.” ― Billy Joel",    "“If everything seems under control, you’re not going fast enough.” — Mario Andretti",    "“There does come a moment when you start saying, ‘I want more,’ and people look at you a little cross-eyed, because it’s loving what you have and also knowing you want to try for more. Sometimes that makes people uncomfortable.” — Ariana DeBose",    "“Trust yourself. You probably know more than you think you do… Trust that you can learn anything.” — Melinda French Gates",    "“I dream it / I work hard / I grind ’til I own it” — Beyoncé",    "“Build your own dreams or someone else will hire you to build theirs.” — Farrah Gray",    "“Definitions belong to the definers, not the defined.” ― Toni Morrison, Beloved",    "“If you want to be a true professional, do something outside yourself.” — Ruth Bader Ginsburg"],
    4: ["“Owning up to your vulnerabilities is a form of strength.” — Lizzo",    "“Very often a change of self is needed more than a change of scene.” — Arthur Christopher Benson",    "“I’ve learned that people will forget what you said, people will forget what you did, but people will never forget how you made them feel.” — Maya Angelou",    "“The reality is: Sometimes you lose. And you’re never too good to lose. You’re never too big to lose. You’re never too smart to lose. It happens. And it happens when it needs to happen. And you need to embrace those things.” — Beyoncé",    "“Even if I don’t reach all my goals, I’ve gone higher than I would have if I hadn’t set any.” — Danielle Fotopoulis",    "“Failure is the condiment that gives success its flavor.” — Truman Capote",    "“You never know which people, places, and experiences are going to shift your perspective until after you've left them behind and had some time to look back.” ― Quinta Brunson",    "“I don't harp on the negative because if you do, then there's no progression. There's no forward movement. You got to always look on the bright side of things, and we are in control. Like, you have control over the choices you make.” — Taraji P. Henson",    "“And how do you know when you’re doing something right? How do you know that? It feels so. What I know now is that feelings are really your GPS system for life. When you’re supposed to do something or not supposed to do something, your emotional guidance system lets you know. The trick is to learn to check your ego at the door and start checking your gut instead.” — Oprah Winfrey",    "“Develop success from failures. Discouragement and failure are two of the surest stepping stones to success.” — Dale Carnegie",    "“You may encounter many defeats, but you must not be defeated. In fact, it may be necessary to encounter the defeats, so you can know who you are, what you can rise from, how you can still come out of it.” ― Maya Angelou",    "“Self-care is really rooted in self-preservation, just like self-love is rooted in honesty. We have to start being more honest with what we need, and what we deserve, and start serving that to ourselves. It can be a spa day! But for a lot of people, it's more like, I need a mentor. I need someone to talk to. I need to see someone who looks like me that's successful, that's doing the things that I want to do, to know that it's possible.” — Lizzo",    "“A dead end street is a good place to turn around.” — Naomi Judd",    "“The only way to do great work is to love what you do. If you haven’t found it yet, keep looking. Don’t settle.” — Steve Jobs",    "“An unexamined life is not worth living.” — Socrates",    "“Life can only be understood backward, but it must be lived forwards.” — Søren Kierkegaard",    "“Self-reflection is a much kinder teacher than regret is. Prioritize yourself by making a habit of it.” — Andrena Sawyer",    "“I hate that word: ‘lucky.’ It cheapens a lot of hard work.” — Peter Dinklage"],
    5: ["Woo girl, need to kick off your shoes / Got to take a deep breath, time to focus on you” — Lizzo",    "To live is the rarest thing in the world. Most people exist, that is all.” ― Oscar Wilde",    "Rivers know this: There is no hurry. We shall get there some day.” ― A.A. Milne",    "It takes courage to grow up and become who you really are.” — e.e. cummings",    "Optimism is a huge asset. We can always use more of it. But optimism isn’t a belief that things will automatically get better; it’s a conviction that we can make things better.” — Melinda French Gates",    "Let nothing happen, just for a bit, let the minutes toll in the stunning air, let us lie on our beds like astronauts, hurtling through space and time.” — Olivia Laing",    "The more I want to get something done the less I call it work.” — Richard Bach",    "There is always light. If only we’re brave enough to see it. If only we’re brave enough to be it.” — Amanda Gorman",    "Someone’s sitting in the shade today because someone planted a tree a long time ago.” — Warren Buffett",    "We must be willing to let go of the life we planned so as to have the life that is waiting for us.” — Joseph Campbell",    "She was learning, quite late, what many people around her appeared to have known since childhood that life can be perfectly satisfying without major achievements.” ― Alice Munro",    "Don’t ever confuse the two, your life and your work. The second is only part of the first.” — Anna Quindlen"],
    6: ["“The individual who says it is not possible should move out of the way of those doing it.” — Tricia Cunningham",    "“The true meaning of life is to plant trees under whose shade you do not expect to sit.” — Nelson Henderson",    "“Success is where preparation and opportunity meet.” — Bobby Unser",    "“Success is the sum of small efforts repeated day in and day out.” — Robert Collier",    "“Before I started, I decided that I’d only pursue this career if my self-worth was dependent on more than celebrity success.” — Beyoncé",    "“People get scared when you try to do something, especially when it looks like you’re succeeding. People do not get scared when you’re failing. It calms them. But when you’re winning, it makes them feel like they’re losing or, worse yet, that maybe they should've tried to do something too, but now it’s too late. And since they didn’t, they want to stop you. You can’t let them.”— Mindy Kaling",    "“Success is liking yourself, liking what you do, and liking how you do it.” — Maya Angelou",    "“Success is a state of mind. If you want success, start thinking of yourself as a success.” — Joyce Brothers",    "“Don’t aim for success if you want it, just do what you love and believe in and it will come naturally.” — David Frost",    "“Whether I fail or succeed, it’s the going for it.” — Jonathan Van Ness",    "“Success only comes to those who dare to attempt.” — Mallika Tripathi",    "“People rarely succeed unless they have fun in what they are doing.” — Dale Carnegie",    "“Always work hard and have fun in what you do because I think that's when you're more successful. You have to choose to do it.” — Simone Biles",    "“Don’t trust any one story of how to become successful.” — Mindy Kaling",    "Regina Borsellino also contributed writing, reporting, and/or advice to this article."],
}
@client.event
async def on_ready():
    print('Bot is ready!')

@client.event
async def on_message(message):
    if message.content.startswith('!quote'):
        # Get the current day of the week (0 = Monday, 6 = Sunday)
        day = datetime.datetime.today().weekday()

        # Select a random quote from the list for the current day
        quote = random.choice(quote_lists[day])
        await asyncio.sleep(1)
        async with message.channel.typing():
            await asyncio.sleep(2)
        await message.delete()
        # Send the quote to the channel
        day_name = calendar.day_name[day]
        embed = discord.Embed(title=f'Daily quote for {day_name}', description=quote, color=0xffa500)
        await message.channel.send(embed=embed)

# Replace YOUR_BOT_TOKEN with your bot's token
client.run(TOKEN)
