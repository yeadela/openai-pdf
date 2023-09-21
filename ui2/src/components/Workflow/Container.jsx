import { memo } from 'react'
import { Box } from './Box'
import { Dustbin } from './Dustbin'
import { HTML5Backend } from 'react-dnd-html5-backend'
import { DndProvider } from 'react-dnd'
export const Container = memo(function Container() {
    return (
        <DndProvider backend={HTML5Backend}>
            <div>
                <div style={{ overflow: 'hidden', clear: 'both' }}>
                    <Dustbin />
                </div>
                <div style={{ overflow: 'hidden', clear: 'both' }}>
                    <Box name="Glass" />
                    <Box name="Banana" />
                    <Box name="Paper" />
                </div>
            </div>
        </DndProvider>
    )
})
