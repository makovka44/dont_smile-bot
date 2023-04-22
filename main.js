const { Client, Intents } = require('discord.js');
const client = new Client({ intents: [Intents.FLAGS.GUILDS, Intents.FLAGS.GUILD_MESSAGES] });

client.once('ready', () => console.log('Ready!'));

// List of 8ball responses
const responses = [
  'It is certain.',
  'It is decidedly so.',
  'Without a doubt.',
  'Yes - definitely.',
  'You may rely on it.',
  'As I see it, yes.',
  'Most likely.',
  'Outlook good.',
  'Yes.',
  'Signs point to yes.',
  'Reply hazy, try again.',
  'Ask again later.',
  'Better not tell you now.',
  'Cannot predict now.',
  'Concentrate and ask again.',
  'Don\'t count on it.',
  'Outlook not so good.',
  'My sources say no.',
  'Very doubtful.'
];

client.on('message', message => {
    if (message.content.startsWith('/ask-me')) {
      // Pick a random response
      const response = responses[Math.floor(Math.random() * responses.length)];
      // Send the response to the channel
      message.channel.send(response);
    }
  });
  
  client.login(process.env.drugi_token);