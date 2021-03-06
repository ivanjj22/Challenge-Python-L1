import React from 'react';

export const ListItem = ({ label, value }) => {
    return (
        <li className="list-group-item d-flex justify-content-between align-items-start">
            <div className="ms-2 me-auto">
                <div className="fw-bold">{label}</div>
                {value}
            </div>
        </li>
    )
}
