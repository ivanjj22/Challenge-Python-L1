import React from 'react';
import { ListItem } from './ListItem';

const labels = {
    "total": "Tiempo total",
    "avg": "Tiempo promedio",
    "min": "Tiempo mínimo",
    "max": "Tiempo máximo",
}

export const Metrics = ({ data }) => {
    return (
        <ol className="list-group list-group-numbered">
            {
                Object.keys(data).map(key => (
                    <ListItem key={key} label={labels[key]} value={data[key]} />
                ))
            }
        </ol>
    )
}
