import React, { useState } from 'react'
import { Input, Form, Button } from "antd"

export default function PublishDrag() {
    const [data, setData] = useState();
    const [form] = Form.useForm();

    return (
        <Form form={form}>
            <Form.Item label="Publish API:" >
                <Input
                    placeholder=""
                    value={data}
                />
            </Form.Item>
            <Form.Item
                wrapperCol={{
                    offset: 16,
                    span: 16,
                }}
            >
                <Button type="primary" htmlType="submit">
                    Save
                </Button>
            </Form.Item>
        </Form>
    )
}
