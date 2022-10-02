import { Bar } from 'react-chartjs-2'

const data = {
    labels: ["Language Acquisition", "Design", "Mathematics", "Physical and health education", "Arts- Music", "Technology", "Science-Chemistry"],
    dataset: [
        {
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