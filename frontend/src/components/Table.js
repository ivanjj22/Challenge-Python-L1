import React from 'react';
import { Row } from './Row';

export const Table = ({ data }) => {
    return (
        <div className="table-responsive">
            <table className="table table-striped ">
                <thead className="table-success">
                    <tr>
                        <th scope="col">Region</th>
                        <th scope="col">Country Name</th>
                        <th scope="col">Language</th>
                        <th scope="col">Time</th>
                    </tr>
                </thead>
                <tbody>
                    {
                        data.map(row => (
                            <Row record={row} key={row.Region} />
                        ))
                    }
                </tbody>
            </table>
        </div>
    )
}
