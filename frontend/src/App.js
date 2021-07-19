import React, { useEffect, useState } from 'react'
import FatalError from './components/FatalError';
import Loading from './components/Loading';
import { Table } from './components/Table';
import { Metrics } from './components/Metrics';
import url from './config';

export const App = () => {

  const [records, setRecords] = useState([]);
  const [metrics, setMetrics] = useState({});
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  useEffect(() => {
    loadData();
  }, []);

  const loadData = () => {
    setLoading(true);
    fetch(url)
      .then((response) => {
        if (response.ok) {
          return response.json();
        } else {
          throw new Error('Something went wrong');
        }
      })
      .then(resp => {
        setRecords(resp.data);
        setMetrics(resp.metrics);
      })
      .catch((error) => setError(error))
      .finally(() => setLoading(false));
  }

  if (error)
    return <FatalError />

  if (loading)
    return <Loading />

  return (
    <div className="container mt-4">
      <h1 className="text-center">Pandas Exercice</h1>
      <hr />
      <Table data={records} />
      <hr />
      <Metrics data={metrics} />
    </div>
  )
}


export default App;
