/*
{
"city": "Bilbao", 
"clouds": 1,
"rain_probability": 0.99, 
"temperature": 15
}
*/
const app = Vue.createApp ({
    data(){
        return{
            city:"Guadalajara",
            day:"hoy",
            clouds:0.2,
            image:"https://ssl.gstatic.com/onebox/weather/64/rain.png",
            temperature: 0
            }
    },
    mounted() {
        this.loadData()
    },
    methods:{
        async loadData() {     
            let endpoint = '' 
            if (this.day === 'hoy') {
                endpoint = 'http://localhost:5000/bilbao'
            }else { 
                endpoint = 'http://localhost:5000/bilbao/' + this.day       
            }
            let response = await fetch(endpoint)
            let external_data = await response.json()
            console.log("loadData", external_data)
            this.city = external_data.city
            this.temperature = external_data.temperature
            this.clouds = external_data.clouds
        }   
    }
})
app.mount("#vue-app")
