import React, { useState, useEffect } from 'react';
// import type { ProColumns } from '@ant-design/pro-table';
// import ProTable from '@ant-design/pro-table';
import { Card, Table } from 'antd';
// import { Link } from 'umi';

export type TableListItem = {
  key: number;
  name: string;
  createdT: string;
  creator: string;
};

const FlowList: React.FC = (props: any) => {
  const [tableData, setTableData] = useState<TableListItem[]>([]);

  const getList = () => {
    setTableData([
      {
        key: 1,
        name: 'Workflow1',
        creator: 'user1',
        createdT: '2022-04-01',
      },
      {
        key: 2,
        name: 'Workflow2',
        creator: 'user1',
        createdT: '2023-04-02',
      },
      {
        key: 3,
        name: 'Workflow3',
        creator: 'user2',
        createdT: '2023-09-03',
      },
    ]);
  };

  useEffect(() => {
    getList();
  }, []);

  const columns = [
    {
      title: 'Workflow Name',
      dataIndex: 'name',
    },
    {
      title: 'Create User',
      dataIndex: 'creator',
    },
    {
      title: 'Create Date',
      dataIndex: 'createdT',
    },
    {
      title: 'Action',
      width: 120,
      render: (_, record, row) => <a onClick={() => viewDetails(row)}>View Details</a>
    },
  ];
  const viewDetails = (row) => {
    props.onChangeTab(1);
    props.setFlow(row);
  }
  return (
    <Card>
      <Table
        columns={columns}
        dataSource={tableData}
        rowKey="key"
      />
    </Card>
  );
};

export default FlowList;
