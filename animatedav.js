const {SlashCommandBuilder, EmbedBuilder, embedLength} = require('discord.js')

module.exports = {
    data: new SlashCommandBuilder()
    .setName('animatedavatar')
    .setDescription('add an animated avatar for me')
    .addAttachmentOption(option => option.setName('avatar').setDescription('avatar to animate').setRequired(true)),
    async execute (interaction, client) {
        const {options} = interaction;
        const avatar = options.getAttachment('avatar')
        if (interaction.user.id == '1119866937946669096') {
            async function sendMessage (message) {
                const embed = new EmbedBuilder()
                .setColor('Gold')
                .setDescription(message)
    
                await interaction.reply({ embeds: [embed], ephemeral: true})
            }
    
            var error;
            await client.user.setAvatar(avatar.url).catch(async err => {
                error = true;
                console.log(err)
                return await sendMessage(`error`)
            })

        } else {
            return;
        }

        if (error) return;
        await sendMessage('I have uploaded your avatar ✌️')

        
    }
}
