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
            data: [7, 9, 10, 4, 12, 6, 8]

        }
    ]
}



function BarChart() {



    return (
        <div>
            <h1>BarChart</h1>

            <Bar data={data} />

        </div>

    )
}

export default BarChart