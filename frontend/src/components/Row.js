import React from 'react';

export const Row = ({ record }) => {
    return (
        <tr>
            <th scope="row">{record["Region"]}</th>
            <td>{record["City Name"]}</td>
            <td>{record["Language"]}</td>
            <td>{record["Time"]}</td>
        </tr>
    )
}
