package com.example

import io.ktor.client.*
import io.ktor.client.engine.cio.*
import io.ktor.client.request.*
import io.ktor.client.statement.*
import io.ktor.http.*
import io.ktor.server.application.*
import kotlinx.serialization.Serializable

import kotlinx.serialization.json.Json

val client = HttpClient(CIO)

@Serializable
data class DiscordMessage(val content: String)

suspend fun sendBotMessage(botToken: String, channelId: String, message: String) {
    val response: HttpResponse = client.post("https://discord.com/api/v10/channels/$channelId/messages") {
        headers {
            append(HttpHeaders.Authorization, "Bot $botToken")
        }
        contentType(ContentType.Application.Json)
        setBody(Json.encodeToString(DiscordMessage(message)))
    }
    println("Odpowiedź: ${response}")
}


suspend fun main(args: Array<String>) {
//    io.ktor.server.netty.EngineMain.main(args)

    val botToken = ""
    val channelId = ""
    sendBotMessage(botToken, channelId, "Cześć, to wiadomość od mojego bota!")
}

fun Application.module() {
    configureRouting()
}
