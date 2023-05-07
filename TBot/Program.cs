using System.Net.Http;
using Newtonsoft.Json;
using Newtonsoft.Json.Linq;

// string token = File.ReadAllText("token.config");
// HttpClient hc = new();
// hc.BaseAddress = new Uri($"https://api.telegram.org/bot{token}/");

// int offset = 0;

// string contentObj = hc.GetStringAsync($"getUpdates?offset={offset}").Result;

// JObject obj = JObject.Parse(contentObj);
// JArray messages = JArray.Parse(obj["result"].ToString());

// for (int i = 0; i < messages.Count; i++)
// {
//     Console.Write($"{messages[i]["message"]["from"]["first_name"]} -> ");
//     Console.WriteLine($"{messages[i]["message"]["text"]}");
    
// }

// System.Console.WriteLine(messages.Count);

string token = File.ReadAllText("token.config");
TelegramBot bot = new TelegramBot(token);

void Updates(TelegramMessageModel msg)
{
    bot.SendMessage(msg.chatId, $"{msg.text}: получено");
}

bot.action = Updates;

bot.Start();

System.Console.WriteLine("++++");


