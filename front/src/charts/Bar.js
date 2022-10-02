import React from 'react'
import { Bar } from 'react-chartjs-2'



import {
    Chart as ChartJS,
    CategoryScale,
    LinearScale,
    BarElement,
    Title,
    Tooltip,
    Legend,
} from 'chart.js';
ChartJS.register(
    CategoryScale,
    LinearScale,
    BarElement,
    Title,
    Tooltip,
    Legend
);

const data = {
    labels: ["Language Acquisition", "Design", "Mathematics", "Physical and health education", "Arts- Music", "Technology", "Science-Chemistry"],
    datasets: [
        {
            label: 'Desempeño anual por generación',
            data: [7, 9, 10, 4, 12, 6, 8],
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(255, 159, 64, 0.2)',
                'rgba(54, 162, 235, 0.2)'
            ]

        }
    ]
}



function BarChart() {



    return (
        <div style={{  }}>


            <Bar data={data} />

        </div>

    )
}

export default BarChart